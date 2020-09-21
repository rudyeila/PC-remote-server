def error_response(error: Exception or str, status=500, toConsole=True): 
    if (toConsole):
        print(error)
    return {"error": str(error)}, status
