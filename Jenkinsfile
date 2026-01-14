pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                script {
                    // Se asume que has configurado la herramienta 'SonarQube Scanner' en Jenkins
                    def scannerHome = tool 'SonarQube Scanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=agenda-goles \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://sonarqube:9000"
                    }
                }
            }
        }

        stage('Build Image') {
            steps {
                echo "Construyendo la imagen..."
                sh 'docker build -t fase1:latest .'
            }
        }

        stage('Run Container') {
            steps {
                echo "Desplegando contenedor..."
                // Borramos el contenedor anterior si existe para evitar errores
                sh 'docker rm -f test-container || true'
                sh 'docker run --name test-container -d fase1:latest'
            }
        }
    }
}
