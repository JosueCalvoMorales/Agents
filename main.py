# main.py - ejemplo mínimo LangGraph
# NOTA: Este es un ejemplo didáctico que muestra la estructura.
from langgraph.graph import StateGraph, END

# Mock: si no tienes LLM configurado, usamos respuestas fijas para probar el flujo
class State(dict):
    pass

def planner(state):
    print("Planner: crea el plan")
    return {"plan":"1) Investigar 2) Redactar 3) Revisar"}

def researcher(state):
    print("Researcher: ejecutando research")
    return {"research":"Hallazgos: cliente X prefiere envíos via MIA y PTY"}

def executor(state):
    print("Executor: generando resultado final")
    return {"result":"Correo listo: Estimado..., ofrecemos capacidades via MIA y PTY..."}

graph = StateGraph(State)
graph.add_node("planner", planner)
graph.add_node("researcher", researcher)
graph.add_node("executor", executor)
graph.set_entry_point("planner")
graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "executor")
graph.add_edge("executor", END)

app = graph.compile()
state = {"task":"Crear correo seguimiento Aeroplus"}
out = app.invoke(state)
print("Resultado final:\n", out.get("result"))
