pipeline {
  agent {
   docker {
      // Make sure you have the latest semgrep-agent
      // This file is tested with semgrep 0.39.1 on Python 3.9.1
      // For the latest agent, use 'docker pull returntocorp/semgrep-agent:v1'
      image 'returntocorp/semgrep-agent:v1'
      args '-u root'
        }
  }
  stages {
    stage('Build') {
        steps {
            sh 'echo "Building..."'
        }
    }

    stage('Semgrep_agent') {
        environment {
            SEMGREP_COMMIT = "${env.GIT_COMMIT}"
            SEMGREP_REPO_NAME = env.GIT_URL.replaceFirst(/^https:\/\/github.com\/(.*).git$/, '$1')
            SEMGREP_REPO_URL = env.GIT_URL.replaceFirst(/^(.*).git$/,'$1')
            SEMGREP_JOB_URL = "${BUILD_URL}"
            SEMGREP_APP_TOKEN = credentials('SEMGREP_APP_TOKEN')
            SEMGREP_DEPLOYMENT_ID = credentials('SEMGREP_DEPLOYMENT_ID')
            SEMGREP_BRANCH = "${GIT_BRANCH}"
            // BASELINE_REF = "${env.GIT_PREVIOUS_COMMIT}"
        }

        steps{
        sh 'python -m semgrep_agent --config "p/r2c-ci" --publish-token $SEMGREP_APP_TOKEN --publish-deployment $SEMGREP_DEPLOYMENT_ID'
      }
   }
  }
 }