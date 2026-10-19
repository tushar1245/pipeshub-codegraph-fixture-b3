def deployer = new Deploy(env: 'staging', services: ['gateway', 'pricing', 'payments'])

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make -C services/native'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    deployer.rollout()
                }
            }
        }
    }
}
