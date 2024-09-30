pipeline {
    agent { label 'python' }

    stages {
        stage('Checkout') {
            steps {
                // Hacer checkout del código
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                // Construir la imagen de Docker
                sh 'docker build -t flask-app-image .'
            }
        }

        stage('Run Flask App') {
            steps {
                // Ejecutar el contenedor y correr la aplicación Flask
                sh 'docker run -d --name flask-app -p 5000:5000 flask-app-image'
            }
        }

        stage('Run Tests') {
            steps {
                // Ejecutar pruebas usando unittest
                // Asumiendo que tu aplicación y las pruebas están configuradas correctamente
                sh 'docker run --rm flask-app-image python -m unittest discover -s tests'
            }
        }

        stage('Cleanup') {
            steps {
                // Detener y eliminar el contenedor
                sh 'docker stop flask-app || true'
                sh 'docker rm flask-app || true'
                // Limpiar la imagen
                sh 'docker rmi flask-app-image || true'
            }
        }
    }
}
