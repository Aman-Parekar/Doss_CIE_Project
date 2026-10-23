
pipeline {
    agent {
        docker {
            image 'python:3.13-slim'
            args '--init'
        }
    }

    options {
        skipDefaultCheckout(true)
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out from configured SCM.'
            }
        }

        stage('Python Environment') {
            steps {
                sh 'python --version'
                sh 'python -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --no-cache-dir -r requirements.txt'
                sh 'python -m pip install --no-cache-dir pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: CampusFix CI pipeline completed.'
        }

        failure {
            echo 'FAILURE: Check the failed stage in Console Output.'
        }

        always {
            echo 'CampusFix CI pipeline execution finished.'
        }
    }
}
