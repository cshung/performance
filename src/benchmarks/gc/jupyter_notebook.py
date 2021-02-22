# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.

# See `docs/jupyter notebook.md` for how to use this file.

#%% setup cell (must run this)

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Sequence

import pandas

from src.analysis.analyze_cpu_samples import (
    chart_cpu_samples_per_gcs,
    show_cpu_samples_metrics,
    TraceReadAndParseUtils,
)
from src.analysis.analyze_joins import (
    analyze_joins_all_gcs_for_jupyter,
    analyze_joins_single_gc_for_jupyter,
    StagesOrPhases,
)
from src.analysis.analyze_single import (
    analyze_single_for_processed_trace,
    analyze_single_gc_for_processed_trace_file,
    SortGCsBy,
)
from src.analysis.chart_individual_gcs import (
    chart_individual_gcs_for_jupyter,
    chart_individual_gcs_histogram_for_jupyter,
)
from src.analysis.chart_utils import (
    basic_chart,
    BasicHistogram,
    BasicLine,
    BasicLineChart,
    chart_histograms_from_fields,
    chart_lines_from_fields,
    chart_heaps,
    Trace,
)
from src.analysis.condemned_reasons import (
    show_brief_condemned_reasons_for_gc,
    show_condemned_reasons_for_jupyter,
    show_condemned_reasons_for_gc_for_jupyter,
)
from src.analysis.enums import Gens
from src.analysis.parse_metrics import (
    parse_run_metrics_arg,
    parse_single_gc_metric_arg,
    parse_single_gc_metrics_arg,
    parse_single_heap_metrics_arg,
)
from src.analysis.process_trace import ProcessedTraces, test_result_from_path
from src.analysis.report import (
    diff_for_jupyter,
    get_gc_metrics_numbers_for_jupyter,
    report_reasons_for_jupyter,
)
from src.analysis.single_gc_metrics import get_bytes_allocated_since_last_gc
from src.analysis.single_heap_metrics import ALL_GC_GENS
from src.analysis.trace_commands import print_events_for_jupyter
from src.analysis.types import GCKind, get_gc_kind, ProcessedTrace, SpecialSampleKind

from src.commonlib.bench_file import ProcessQuery, Vary
from src.commonlib.collection_util import repeat
from src.commonlib.document import Cell, handle_doc, Row, single_table_document, Table
from src.commonlib.option import non_null
from src.commonlib.result_utils import unwrap
from src.commonlib.type_utils import enum_value, with_slots
from src.commonlib.util import add_extension, bytes_to_mb, get_percent


ALL_TRACES = ProcessedTraces()


def get_trace_with_everything(
    path: Path, process: ProcessQuery = None, dont_cache: bool = False
) -> ProcessedTrace:
    return unwrap(
        ALL_TRACES.get(
            test_result=test_result_from_path(path, process),
            # TODO: disabling mechanisms and join info for now
            # as it doesn't work without updating TraceEvent
            need_mechanisms_and_reasons=False,
            need_join_info=False,
            dont_cache=dont_cache,
        )
    )


def show_summary(trace: ProcessedTrace) -> None:
    print(f"{trace.NumberGCs} GCs")
    for k, v in trace.number_gcs_in_each_generation.items():
        print(f"  {k.name}: {v}")
    print(f"{trace.HeapCount} heaps")
    for m in ("HeapSizeAfterMB_Mean", "HeapSizeAfterMB_Max"):
        print(f"{m}: {trace.unwrap_metric_from_name(m)}")
    # TODO: how to get mean/max memory load? Is it possible?

    metrics: Sequence[str] = ("PauseDurationMSec", "PromotedMBPerSec", "HeapSizeAfterMB")
    num_metrics = len(metrics)
    kind_to_metric_to_values: List[List[List[float]]] = [
        [[] for _ in range(num_metrics)] for _ in range(4)
    ]
    for gc in trace.gcs:
        gc_kind = get_gc_kind(gc)
        for metric_index, metric in enumerate(metrics):
            metric_index_to_values = kind_to_metric_to_values[enum_value(gc_kind)]
            values = metric_index_to_values[metric_index]
            values.append(gc.unwrap_metric_from_name(metric))

    for kind in GCKind:
        histograms: List[BasicHistogram] = []
        for metric_index, metric in enumerate(metrics):
            histograms.append(
                BasicHistogram(
                    values=kind_to_metric_to_values[enum_value(kind)][metric_index],
                    name=metric,
                    x_label=kind.name,
                )
            )

        basic_chart(histograms)

_BENCH = Path("bench")
_SUITE = Path("bench") / "suite"
_TRACE_PATH = _SUITE / "markof.yaml"

metrics_data = get_gc_metrics_numbers_for_jupyter(
    traces=ALL_TRACES,
    bench_file_path=_TRACE_PATH,
    run_metrics=parse_run_metrics_arg(("important",)),
    machines=None,
)

data_frame = pandas.DataFrame.from_dict(metrics_data)

data_frame.describe()

# %%
