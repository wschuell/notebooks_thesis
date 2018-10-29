set -e

configs_gen

strings=(
"chapters/naminggame/normal"
"chapters/naminggame/VU"
"chapters/naminggame/wordchoice"
"chapters/naminggame/homonymy"
"chapters/naminggame/accpol"
"chapters/topicchoice/normal"
"chapters/topicchoice/exploexplo"
"chapters/topicchoice/explobias"
"chapters/topicchoice/STW"
"chapters/topicchoice/STN"
"chapters/topicchoice/ST2"
"chapters/topicchoice/ST_HC"
"chapters/topicchoice/MCW"
"chapters/topicchoice/MCN"
"chapters/topicchoice/MC2"
"chapters/topicchoice/MC_HC"
"chapters/topicchoice/IGW"
"chapters/topicchoice/IGN"
"chapters/topicchoice/chunksW"
"chapters/topicchoice/chunksN"
"chapters/topicchoice/chunks_HC"
"chapters/topicchoice/comparison"
"chapters/topicchoice/comparisonW"
"chapters/topicchoice/comparisonM"
"chapters/topicchoice/comparisonHC"
"chapters/laps/previous"
"chapters/laps/normal"
"chapters/laps/lapsWT"
"chapters/laps/lapsNT"
"chapters/laps/lapsHC"
"chapters/laps/lapsT2"
"chapters/laps/entropyWT"
"chapters/laps/entropyNT"
# "chapters/laps/entropyT2"
"chapters/laps/lapsscaling"
"chapters/laps/coherenceWT"
"chapters/laps/coherenceNT"
"chapters/laps/coherenceT2"
# "chapters/laps/coherenceMB"
# # "chapters/laps/coherencescaling"
"chapters/replace/replace"
"chapters/replace/decay"
"chapters/theory/tconv_100"
"chapters/theory/perf"
"chapters/theory/perf2"
)

parallel --jobs 8 bash exec_one.sh ::: ${strings[@]}
