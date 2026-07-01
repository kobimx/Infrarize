"""Constants for the Infrarize config flow and platforms."""
from __future__ import annotations

# ── Sentinels ──────────────────────────────────────────────────────────────────
MANUAL_ENTRY_SENTINEL = "__manual__"
ALL_CONTROLLERS_SENTINEL = "Any"
INDEX_FILENAME = "codes_index.json"

# ── Config-entry data keys ─────────────────────────────────────────────────────
CONF_PLATFORM = "platform"
CONF_DEVICE_CODE = "device_code"
CONF_CONTROLLER_DATA = "controller_data"
CONF_DELAY = "delay"
CONF_DEVICE_NAME = "name"
CONF_TEMPERATURE_SENSOR = "temperature_sensor"
CONF_HUMIDITY_SENSOR = "humidity_sensor"
CONF_POWER_SENSOR = "power_sensor"
CONF_POWER_SENSOR_RESTORE_STATE = "power_sensor_restore_state"
CONF_DEVICE_CLASS = "device_class"
CONF_SOURCE_NAMES = "source_names"

# ── Defaults ───────────────────────────────────────────────────────────────────
DEFAULT_DELAY = "0.5"

# ── Platform choices ───────────────────────────────────────────────────────────
PLATFORMS: dict[str, str] = {
    "climate":      "Climate (Air Conditioner / Heat Pump)",
    "fan":          "Fan",
    "media_player": "Media Player (TV / Receiver)",
    "light":        "Light",
}

PLATFORM_SUBDIR: dict[str, str] = {
    "climate":      "climate",
    "fan":          "fan",
    "media_player": "media_player",
    "light":        "light",
}

DEFAULT_DEVICE_NAMES: dict[str, str] = {
    "climate":      "Infrarize Climate",
    "fan":          "Infrarize Fan",
    "media_player": "Infrarize Media Player",
    "light":        "Infrarize Light",
}

# ── Controller metadata ────────────────────────────────────────────────────────
# Controllers whose device identifier is a Home Assistant remote entity ID.
# These get an EntitySelector in the UI instead of a plain text field.
ENTITY_BASED_CONTROLLERS: frozenset[str] = frozenset({"Broadlink", "Xiaomi"})

CONTROLLER_HINTS: dict[str, str] = {
    "Broadlink": "Select the Broadlink remote entity that will send IR commands.",
    "Xiaomi":    "Select the Xiaomi remote entity that will send IR commands.",
    "MQTT":      "Enter the MQTT topic to publish IR commands to (e.g. zigbee2mqtt/ir_blaster/set).",
    "LOOKin":    "Enter the LOOKin device IP address (e.g. 192.168.1.42).",
    "ESPHome":   "Enter the ESPHome remote service name (e.g. esphome_ir_blaster).",
}

