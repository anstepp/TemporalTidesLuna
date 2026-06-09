def test_range():
    # 1. Define array of inputs
    test_values = [4, 10, 15, 20]
    
    # 2. Loop through them one by one
    for val in test_values:
        # custom error message so we know which number failed
        assert val <= 15, f"Test failed for value: {val}"