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
                // Construir la imagen de Docker (usando bat en lugar de sh para Windows)
                bat 'docker build -t flask-app-image .'
            }
        }

        stage('Run Flask App') {
            steps {
                // Ejecutar el contenedor y correr la aplicación Flask
                bat 'docker run -d --name flask-app -p 5000:5000 flask-app-image'
            }
        }

        stage('Run Tests') {
            steps {
                // Ejecutar pruebas usando unittest dentro del contenedor
                // En Windows, usa docker exec para ejecutar los tests directamente en el contenedor
                bat 'docker exec flask-app python -m unittest discover -s tests > test-results.xml'
            }
            post {
                always {
                    // Publicar los resultados de las pruebas
                    junit 'test-results.xml'
                }
            }
        }

        stage('Cleanup') {
            steps {
                // Detener y eliminar el contenedor
                bat 'docker stop flask-app || exit 0'
                bat 'docker rm flask-app || exit 0'
                // Limpiar la imagen
                bat 'docker rmi flask-app-image || exit 0'
            }
        }
    }

    post {
        failure {
            // Enviar notificaciones en caso de fallo
            mail to: 'devops@example.com',
                 subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                 body: "Check Jenkins for details: ${env.BUILD_URL}"
        }
    }
}
