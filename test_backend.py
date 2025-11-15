from backend import calc_aqi_level
from config import AQI_INTERVALS


def interval_level_calculation( concentration: float, interval: str, expected_level: int ):
    """
    Generic test function for AQI level calculation.

    Args:
        concentration (float): The pollutant concentration to test.
        interval (str): The pollutant type (e.g., "co", "no2", etc.).
        expected_level (int): The expected AQI level for the given concentration.

    Returns:
        None
    """

    intervals = AQI_INTERVALS[interval]
    calculated_level = calc_aqi_level(concentration, intervals)
    assert calculated_level == expected_level

def test_co_level_calculation():
    """
    Tests CO level calculations.
    CO concentration of "684.85" should be Level 1 ("Good").
    """

    interval_level_calculation( 684.85, "co", 1 )

def test_no2_level_calculation():
    """
    Tests NO2 level calculations.

    NO2 concentration of "50" should be Level 2 ("Good").
    """

    interval_level_calculation(50, "no2", 2)

def test_O3_level_calculation():
    """
    Tests O3 level calculations.

    O3 concentration of "250" should be Level 3 ("Moderate").
    """

    interval_level_calculation(250, "o3", 3)


def test_so2_level_calculation():
    """
    Tests the case we found in the debugger.

    SO2 concentration of "77" should be Level 2 ("Good").
    """

    interval_level_calculation(77, "so2", 2)

def test_pm2_5_level_calculation():
    """
    Tests PM2.5 level calculations.

    PM2.5 concentration of "80" should be Level 3 ("Moderate").
    """

    interval_level_calculation(80, "pm2_5", 3)

def test_pm10_level_calculation():
    """
    Tests PM10 level calculations.

    PM10 concentration of "120" should be Level 2 ("Good").
    """

    interval_level_calculation(120, "pm10", 2)