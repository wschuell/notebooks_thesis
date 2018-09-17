strings=(
"chapters/naminggame/normal"
"chapters/naminggame/VU"
"chapters/naminggame/wordchoice"
"chapters/naminggame/homonymy"
"chapters/naminggame/accpol"
"chapters/topicchoice/exploexplo"
"chapters/topicchoice/explobias"
"chapters/topicchoice/STW"
"chapters/topicchoice/STN"
"chapters/topicchoice/ST2"
"chapters/topicchoice/MCW"
"chapters/topicchoice/MCN"
"chapters/topicchoice/IGW"
"chapters/topicchoice/IGN"
)
for folder in "${strings[@]}"; do
    echo "$folder"
    (cd $folder && hd_metaexp ) || (echo "$folder"; exit 1 ) || exit 1
done