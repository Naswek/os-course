#!/usr/bin/env bash
set -euo pipefail

N=10
ITER=1
OUT=my_files/results_read.csv
echo "timestamp,graph,run_id,wall_time_s,user_time_s,sys_time_s,vol_ctx,invol_ctx,minflt,majflt" > "$OUT"

graphs=(graph-seq.bin graph-rand.bin)
for i in $(seq 1 "$N"); do
	  for g in "${graphs[@]}"; do
		      ts=$(date +%s)
		          /usr/bin/time \
				-f "$ts,$g,$i,%e,%U,%S,%w,%c,%R,%F" \
					-a -o "$OUT" \
					 ./out/graph_traverse --no-cache "$ITER" "$g" \
						     > /dev/null
			    done
		    done
