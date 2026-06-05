"""Tests for the Quantum Console"""

import pytest
from src.console import QuantumConsole


class TestQuantumConsole:
    """Test cases for QuantumConsole class."""

    def test_initialization(self):
        """Test that console initializes correctly."""
        console = QuantumConsole()
        assert console.initialized is True
        assert console.version == "0.1.0"

    def test_execute_command(self):
        """Test command execution."""
        console = QuantumConsole()
        result = console.execute("test_command")
        assert result == "Executing: test_command"

    def test_uninitialized_execution(self):
        """Test that execution fails on uninitialized console."""
        console = QuantumConsole()
        console.initialized = False

        with pytest.raises(RuntimeError):
            console.execute("test_command")

    def test_repr(self):
        """Test string representation."""
        console = QuantumConsole()
        assert "QuantumConsole" in repr(console)
        assert "0.1.0" in repr(console)
