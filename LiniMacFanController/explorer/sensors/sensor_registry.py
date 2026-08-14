"""Classification rules for Apple SMC temperature sensors.

SMC keys are model-specific and a machine can expose the same physical reading
under more than one key.  Keep the small, useful set of thermal readings in
the default monitor and use aliases only when their preferred key is absent.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, TypeVar


class SensorClassification(Enum):
    """Whether a sensor should be shown by the default monitor."""

    PRIMARY = "primary"
    ALIAS = "alias"
    HIDDEN = "hidden"


@dataclass(frozen=True)
class SensorDefinition:
    name: str
    logical_key: str
    classification: SensorClassification


# These names are intentionally conservative: only readings that identify a
# useful thermal source are shown.  Other opaque SMC keys remain available on
# ``HardwareExplorer.sensors`` for diagnostics, but do not clutter the view.
SENSOR_DEFINITIONS = {
    "TA0P": SensorDefinition("Ambient", "ambient", SensorClassification.PRIMARY),
    "TA0V": SensorDefinition("Ambient", "ambient", SensorClassification.ALIAS),
    "TC0C": SensorDefinition("CPU Core", "cpu_core", SensorClassification.PRIMARY),
    "TC1C": SensorDefinition("CPU Core", "cpu_core", SensorClassification.ALIAS),
    "TC0H": SensorDefinition("CPU Heatsink", "cpu_heatsink", SensorClassification.PRIMARY),
    "TG0D": SensorDefinition("GPU Diode", "gpu", SensorClassification.PRIMARY),
    "TG0H": SensorDefinition("GPU Diode", "gpu", SensorClassification.ALIAS),
    "TG0p": SensorDefinition("GPU Diode", "gpu", SensorClassification.ALIAS),
    "Tp2H": SensorDefinition("Power Supply", "power_supply", SensorClassification.PRIMARY),
}

# Kept as a compatibility-friendly name for callers that only need labels.
KNOWN_SENSORS = {key: definition.name for key, definition in SENSOR_DEFINITIONS.items()}


def definition_for(key: str) -> SensorDefinition:
    """Return the classification for an SMC key, hiding unknown keys by default."""
    return SENSOR_DEFINITIONS.get(
        key,
        SensorDefinition(key, key, SensorClassification.HIDDEN),
    )


SensorLike = TypeVar("SensorLike", bound=object)


def select_display_sensors(sensors: Iterable[SensorLike]) -> list[SensorLike]:
    """Choose one canonical sensor for each useful physical reading.

    A primary key wins over any alias.  An alias is retained as a fallback on
    hardware that exposes it without the primary key.
    """
    selected: dict[str, SensorLike] = {}
    selected_classifications: dict[str, SensorClassification] = {}

    for sensor in sensors:
        definition = definition_for(sensor.key)
        if definition.classification is SensorClassification.HIDDEN:
            continue

        current = selected_classifications.get(definition.logical_key)
        if current is None or (
            definition.classification is SensorClassification.PRIMARY
            and current is SensorClassification.ALIAS
        ):
            selected[definition.logical_key] = sensor
            selected_classifications[definition.logical_key] = definition.classification

    return list(selected.values())
