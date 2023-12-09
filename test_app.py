from backend.combined_yt_gpt import main_combined, get_difficulty_and_time


def test_main_combined():
    """
    Test main_combined function.
    Checks to verify that the function returns steps and a youtube link.
    """
    steps, youtube_link = main_combined()
    assert steps
    assert youtube_link


def test_get_difficulty_and_time():
    """
    Test get_difficulty_and_time function.
    Checks to verify valid time and difficulty are returned.
    """
    difficulty, time = get_difficulty_and_time()
    assert difficulty
    assert time