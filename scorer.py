def judge(question, expects, answer, results) -> bool:
    if not expects:
        return False
    
    # Safely convert answer to an empty string if it's None, then lower both
    clean_answer = (answer or "").lower()
    clean_expects = expects.strip().lower()
    
    return clean_expects in clean_answer