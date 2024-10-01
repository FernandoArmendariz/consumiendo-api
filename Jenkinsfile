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
    }

    post {
        failure {
            mail to: 'devops@example.com',
                 subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                 body: "Check Jenkins for details: ${env.BUILD_URL}"
        }

        success {
            steps {
                echo 'Pipeline ejecutado correctamente!'
            }
        }

        always {
            echo 'Pipeline finalizado!'
            steps {
                bat 'docker stop flask-app || exit 0'
                bat 'docker rm flask-app || exit 0'
                bat 'docker rmi flask-app-image || exit 0'
            }
        }
    }
}
