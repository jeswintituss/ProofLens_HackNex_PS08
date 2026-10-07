import io
import contextlib

def execute_code(code, df):
    output = io.StringIO()
    safe_builtins = {
        "print": print, "len": len, "min": min, "max": max,
        "sum": sum, "round": round, "str": str, "int": int, "float": float
    }
    try:
        namespace = {"df": df, "__builtins__": safe_builtins}
        with contextlib.redirect_stdout(output):
            exec(code, namespace, namespace)
        return {"success": True, "output": output.getvalue(), "error": None}
    except Exception as e:
        return {"success": False, "output": output.getvalue(), "error": str(e)}
