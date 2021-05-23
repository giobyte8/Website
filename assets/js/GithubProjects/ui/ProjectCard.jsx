import React, { useState, useEffect } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCodeBranch, faStar } from '@fortawesome/free-solid-svg-icons'

import { getProjectLangs } from '../services/GithubService'

const langLogos = {
    'bash': '/img/icons/icons8-bash.svg',
    'html': '/img/icons/icons8-html-5.svg',
    'java': '/img/icons/icons8-java.svg',
    'javascript': '/img/icons/icons8-javascript.svg',
    'python': '/img/icons/icons8-python.svg',
}

const ProjectCard = ({
    name,
    description,
    stargazersCount,
    forksCount,
    htmlUrl
}) => {

    const [lang, setLang] = useState(null)

    useEffect(async () => {
        if (!lang) {
            const langs = await getProjectLangs(name)
            if (langs) {
                setLang(Object.keys(langs)[0])
            }
        }
    })

    const makeCodeLangLogo = () => {
        if (!lang) {
            return ''
        }

        if (!langLogos[lang.toLowerCase()]) {
            return <small>{ lang }</small>
        }

        const url = langLogos[lang.toLowerCase()]
        return <>
            <img src={ url } alt="" width='24px'/>
            <small>&nbsp;{ lang }</small>
        </>
    }

    const makeStarsgazersCounter = () => {
        if (!stargazersCount) {
            return ''
        }

        return <small>
            <FontAwesomeIcon icon={ faStar }/>
            &nbsp;
            { stargazersCount }
        </small>
    }

    const makeForksCount = () => {
        if (!forksCount) {
            return ''
        }

        return <small>
            { stargazersCount
                ? <>&nbsp;&nbsp;</>
                : ''
            }
            <FontAwesomeIcon icon={ faCodeBranch }/>
            &nbsp;
            { forksCount }
        </small>
    }

    const navigateToRepo = () => {
        window.open(htmlUrl, '_blank')
    }


    return <div className='col-12 col-md-6 col-lg-4 mb-3' onClick={ () => navigateToRepo() }>
        <div className="h-100 card project-card">
            <div className="card-body">
                <h5 className="card-title">{ name }</h5>
                <p className="card-text">{ description }</p>
            </div>
            <div className="card-footer">
                <div className="row">
                    <div className="col-7">
                        { makeCodeLangLogo() }
                    </div>

                    <div className="col-5 text-end">
                        { makeStarsgazersCounter() }
                        { makeForksCount() }
                    </div>
                </div>

            </div>
        </div>
    </div>
}

export default ProjectCard
