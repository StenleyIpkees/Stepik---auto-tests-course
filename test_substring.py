def test_substring(full_string, substring):
    assert substring in full_string, "expected '" + substring + "' to be substring of '" + full_string + "'"