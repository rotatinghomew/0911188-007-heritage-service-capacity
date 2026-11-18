import json
from .attendance import arrivals
from .capacity import staffing
from .sampling import response_counts


def run_workbench(action, directory, key, ledger):
    source = json.loads((directory / 'workbench.json').read_text())
    if action == 'survey':
        return response_counts(source['sample_frames'], source['responses'], key)
    visits = arrivals(source['gate_log'], source['calendar'])
    if action == 'attendance':
        return visits
    return staffing(source['calendar'], visits)
