pipeline {
    agent any

    environment {
        SERVICE_NAME = 'app-goles'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                echo "Construyendo la imagen de Docker usando Compose..."
                // Usamos 'docker compose' sin guion para ser consistentes
                sh "docker compose build ${SERVICE_NAME}"
            }
        }

        stage('Deploy App') {
            steps {
                echo "Desplegando la aplicación..."
                sh "docker compose up -d --force-recreate ${SERVICE_NAME}"
            }
        }

        stage('Verify') {
            steps {
                echo "Estado de los contenedores:"
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline finalizado con éxito. La app está corriendo.'
        }
        failure {
            echo '❌ El pipeline falló. Revisa la consola para más detalles.'
        }
    }
}
