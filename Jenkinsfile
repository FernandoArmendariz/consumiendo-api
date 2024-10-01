pipeline {
    agent { label 'python' }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Construir imagen Docker') {
            steps {
                bat 'docker build --no-cache -t flask-app-image .'
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat 'pip install requirements.txt'
            }
        }

        stage('ejecutar aplicación Flask') {
            steps {
                bat 'docker run -d --name flask-app -p 5000:5000 flask-app-image'
            }
        }

        stage('Correr Tests') {
    steps {
        // Ejecutar pruebas y generar archivo XML para Jenkins
        bat 'docker exec flask-app python -m xmlrunner discover -s tests -o tests'
        }
        post {
            always {
                // Publicar los resultados de las pruebas
                junit 'tests/*.xml'
            }
        }
    }

        stage('Limpieza') {
            steps {
                bat 'docker stop flask-app || exit 0'
                bat 'docker rm flask-app || exit 0'
                bat 'docker rmi flask-app-image || exit 0'
            }
        }
    }

    post {
        failure {
            mail to: 'devops@example.com',
                 subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                 body: "Check Jenkins for details: ${env.BUILD_URL}"
        }
    }
}
