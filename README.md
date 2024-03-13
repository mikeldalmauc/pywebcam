
## Como arrancar el entorno de desarrollo

1. Ejecuta `docker compose up` sobre el directorie del fichero docker-compose.yml
2. Accede a la GUI web de jupyter notebook para modificar el script de python 

## Captura de las imágenes

Capturar las imagenes puede ser un reto cuando es un contendor de docker que ejecuta nuestro script de python. 

### Cámara integrada

El caso más sencillo, la cámara se mapea como un [devices](https://stackoverflow.com/questions/44852484/access-webcam-using-opencv-python-in-docker) o [volumen](https://gist.github.com/enric1994/7ab05985f775cb2954de6c30b72b07f9) en el docker-compose y se accede desde python de la siguiente manera:

```python
video_capture = cv2.VideoCapture(0)
```

### Cámara ip

En el caso de no poder mapear el dispositivo de la camara en docker-compose utilzando el atributo [devices](https://stackoverflow.com/questions/44852484/access-webcam-using-opencv-python-in-docker) o [montando el volumen](https://gist.github.com/enric1994/7ab05985f775cb2954de6c30b72b07f9)  */dev/video0:/dev/video0*. 

Un solucción es utilizar un servicio de camara por IP. Esta solucción tiene la ventaja de ser más flexible de cara al uso de camaras no integradas que incluyen video por IP o como workaround en caso de trabajar con windows-docker y no poder mapear la camara directamente. 

1. Descarga el ejecutable que corresponda a tu SO del [siguiente repo](https://github.com/gen2brain/cam2ip) y ejecutalo.


2. Usando tu IP local y puerto del servicio accede a al cámara desde el script de python.

```python
cap = cv2.VideoCapture('http://192.168.56.1:56000/mjpeg')
```

## Entorno de producción

De cara a la puesta en producción, se ha de liberar la aplicación de todas las dependencias de desarrollo que no sean necesarias tales como jupyter notebook.