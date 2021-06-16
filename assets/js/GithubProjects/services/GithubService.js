import { Octokit } from '@octokit/core'
import * as params from '@params'


const username = 'giobyte8'
const featuredProjectsRepos = [
    'watchlist',
    'posforpeople',
    'sigma',
    'pydocker',
    'fxformgenerator',
    'rtspviewer'
]

const octokit = new Octokit({
    auth: params.GH_KEY
})

export const getFeaturedProjects = async () => {
    let repos = []

    for (let repoName of featuredProjectsRepos) {
        let response = await octokit.request('GET /repos/{owner}/{repo}', {
            owner: username,
            repo: repoName
        });

        if (response.status === 200) {
            repos.push(response.data)
        }
    }

    return repos
}

export const getProjectLangs = async (repoName) => {
    const response = await octokit.request(
        'GET /repos/{owner}/{repo}/languages',
        {
            owner: username,
            repo: repoName
        }
    );

    if (response.status === 200) {
        return response.data
    }

    return null;
}
