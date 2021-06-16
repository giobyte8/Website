import * as React from 'react'
import { useState, useEffect } from 'react'

import ProjectCard from './ProjectCard'
import { getFeaturedProjects } from '../services/GithubService'

const FeaturedProjectsApp = () => {
    const [projects, setProjects] = useState(null);

    useEffect(async () => {
        if (!projects) {
            setProjects(await getFeaturedProjects())
        }
    })

    return <div className="row">
        { projects 
            ? projects.map(project => <ProjectCard
                    key={ project.id }
                    name={ project.name }
                    description={ project.description }
                    stargazersCount={ project.stargazers_count }
                    forksCount={ project.forks_count }
                    htmlUrl={ project.html_url }
                />
              )
            : <span>Loading ...</span> 
        }
    </div>
}

export default FeaturedProjectsApp
