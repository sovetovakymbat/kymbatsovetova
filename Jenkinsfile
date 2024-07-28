pipeline {
    agent any
    environment {
        // Replace 'github-token-id' with the ID of the credential in Jenkins that stores the GitHub personal access token
        GITHUB_TOKEN = credentials('github-token-id')
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/yourusername/your-repo.git', credentialsId: 'github-token-id'
            }
        }
        stage('Build') {
            steps {
                script {
                    // Install dependencies
                    sh 'npm install'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh 'npm test'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy application (replace with your deployment script)
                    sh 'npm run deploy'
                }
            }
        }
    }
    post {
        always {
            // Clean up after pipeline execution
            cleanWs()
        }
        success {
            // Notify success
            echo 'Pipeline completed successfully'
        }
        failure {
            // Notify failure
            echo 'Pipeline failed'
        }
    }
}
