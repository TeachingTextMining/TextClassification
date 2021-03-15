El cuaderno está concebido para su ejecución mediante Jupyter, utilizando contenedores Docker. 

(i)	crear la imagen
docker build -f Dockerfile -t pipeline_sa:latest .

(ii) lanzar contenedor + jupyter
docker run -it -p 8888:8888 --volume="[host path]:/[container path]" [image id] jupyter notebook --notebook-dir=[container path] --ip 0.0.0.0 --no-browser --allow-root

    Por ejemplo, suponiendo que esta carpeta se encuentra en "C:\nlp\SA-Transformers-Training-FineTuning"  en una PC Windows, y que se desea montar en "/nlp" dentro del contenedor, el comando quedaría:
	
	docker run -it -p 8888:8888 --volume="/C/nlp/SA-Transformers-Training-FineTuning/:/nlp" transformers_sa:latest jupyter notebook --notebook-dir=/nlp --ip 0.0.0.0 --no-browser --allow-root --NotebookApp.token="sa-pipeline-review"
	
(iii) abrir navegador y acceder a http://localhost:8888?token=sa-pipeline-review