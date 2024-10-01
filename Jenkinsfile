pipeline {
    agent { label 'python' }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install unittest-xml-reporting'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build --no-cache -t flask-app-image .'
            }
        }


        stage('Run Flask App') {
            steps {
                bat 'docker run -d --name flask-app -p 5000:5000 flask-app-image'
            }
        }

        stage('Run Tests') {
    steps {
        // Ejecutar pruebas y generar archivo XML para Jenkins
        bat 'docker exec flask-app python -m xmlrunner discover -s tests -o tests'
        }
        post {
            always {
                // Publicar los resultados de las pruebas
                junit 'test/*.xml'
            }
        }
    }

        stage('Cleanup') {
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
