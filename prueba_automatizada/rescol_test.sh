# Definir variables
EXECUTABLE="/home/alazcano/Rescolants-master/prueba_automatizada/rescol_test.sh"
INPUT_FILE="/home/alazcano/Rescolants-master/Instancias/Instancias_default/CasoRealMediano.txt"
INSTANCE_NAME=$(basename "$INPUT_FILE" .txt) # Nombre de la instancia sin extensiÃ³n
METODO="0"
ITER_MAX="1000"
NUM_HORMIGAS="26"
EPOCAS="1"
salida_Floyd_Warshall="salida-Floyd-Warshall"

BETA0="--beta0"
ALFA="4.99"
RHO="0.3"
TAU="2.06"

USAR_ITERACIONES="--usar-iteraciones"
USAR_LIMITADOR="--usar-limitador"
VALOR_LIMITADOR="1"
SILENCE="--silence"
DIR_SALIDA="./resultados"
PREFIJO_SALIDA="nuevos"
RESCOL="--rescol"

# Ejecutar el comando 10 veces con la primera semilla fija y las siguientes secuenciales
SEMILLA=1234567
for i in {0..19}; do
  OUTPUT_FILE="${INSTANCE_NAME}_$SEMILLA.txt"
  echo "Ejecutando con semilla: $SEMILLA, salida: $OUTPUT_FILE"
  $EXECUTABLE $INPUT_FILE --metodo $METODO  --alfa $ALFA --rho $RHO --tau-as $TAU --iter-max $ITER_MAX --num-hormigas $NUM_HORMIGAS --epocas $EPOCAS $salida_Floyd_Warshall $BETA0 $USAR_ITERACIONES $USAR_LIMITADOR --valor-limitador $VALOR_LIMITADOR $SILENCE --semilla $SEMILLA --dir-salida $DIR_SALIDA --prefijo-salida $PREFIJO_SALIDA --semilla $SEMILLA $RESCOL > "$OUTPUT_FILE"
  SEMILLA=$((SEMILLA + 1))
done