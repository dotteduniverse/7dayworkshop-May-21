#!/usr/bin/env python3
"""
MCP Time Server – A simple Model Context Protocol (MCP) style server.

This server exposes a tool to get the current time in different timezones.
It can be extended to serve as a context provider for AI agents.

Usage (standalone):
    python mcp_time_server.py

Then call with JSON-RPC style messages over stdio or HTTP.
"""

import json
import sys
import datetime
from typing import Dict, Any

# Mapping of timezone names to UTC offsets (hours)
TIMEZONES = {
    "UTC": 0,
    "IST": 5.5,      # India Standard Time
    "EST": -5,       # Eastern Standard Time
    "CST": -6,       # Central Standard Time
    "PST": -8,       # Pacific Standard Time
    "GMT": 0,
    "CET": 1,        # Central European Time
    "AEST": 10,      # Australian Eastern Standard Time
}


def get_current_time(timezone: str = "UTC") -> Dict[str, Any]:
    """
    Get the current date and time in the specified timezone.

    Args:
        timezone: Timezone name (UTC, IST, EST, CST, PST, GMT, CET, AEST)

    Returns:
        Dictionary with status, timezone, current_time, and utc_offset
    """
    tz_upper = timezone.upper()
    if tz_upper not in TIMEZONES:
        return {
            "status": "error",
            "message": f"Unknown timezone: {timezone}. Supported: {list(TIMEZONES.keys())}"
        }

    offset_hours = TIMEZONES[tz_upper]
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    local_time = now_utc + datetime.timedelta(hours=offset_hours)

    return {
        "status": "success",
        "timezone": tz_upper,
        "current_time": local_time.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_offset": f"{offset_hours:+g} hours",
        "timestamp_utc": now_utc.isoformat()
    }


def list_timezones() -> Dict[str, Any]:
    """List all supported timezones."""
    return {
        "status": "success",
        "supported_timezones": list(TIMEZONES.keys())
    }


# MCP Tool definitions (for agent registration)
TOOL_DEFINITIONS = [
    {
        "name": "get_current_time",
        "description": "Get the current date and time in a specific timezone. Input should be a timezone name like 'UTC', 'IST', 'EST'.",
        "parameters": {
            "type": "object",
            "properties": {
                "timezone": {
                    "type": "string",
                    "description": "Timezone name (UTC, IST, EST, CST, PST, GMT, CET, AEST)",
                    "default": "UTC"
                }
            }
        }
    },
    {
        "name": "list_timezones",
        "description": "List all supported timezones.",
        "parameters": {}
    }
]


def handle_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle a JSON-RPC style request.

    Expected format:
        {"method": "get_current_time", "params": {"timezone": "IST"}, "id": 1}
        or
        {"method": "list_timezones", "id": 2}
    """
    method = request.get("method")
    params = request.get("params", {})
    request_id = request.get("id")

    if method == "get_current_time":
        timezone = params.get("timezone", "UTC")
        result = get_current_time(timezone)
    elif method == "list_timezones":
        result = list_timezones()
    else:
        result = {"status": "error", "message": f"Unknown method: {method}"}

    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": result
    }


def run_stdio_server():
    """Run MCP server over stdin/stdout (for integration with agents)."""
    print("[MCP Time Server] Running on stdio. Waiting for requests...", file=sys.stderr)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            response = handle_request(request)
            print(json.dumps(response))
            sys.stdout.flush()
        except json.JSONDecodeError as e:
            error_response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {e}"}
            }
            print(json.dumps(error_response))
            sys.stdout.flush()


if __name__ == "__main__":
    # Simple test if run directly
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Testing MCP Time Server...")
        print(get_current_time("IST"))
        print(list_timezones())
    else:
        # Run as stdio server for agent integration
        run_stdio_server()