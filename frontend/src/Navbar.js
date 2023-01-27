import { Link, useMatch, useResolvedPath } from "react-router-dom"

export default function Navbar() {
    return (
    <nav className="nav">
        <Link to="/" className="site-title"> Midwest Conference Analytics
        </Link>
        <ul>
            <CustomLink to = "/baseball">Baseball</CustomLink>
            <CustomLink to = "/football">Football</CustomLink>
        </ul>
   </nav>
   )
}

function CustomLink({to, children, ...props }){
    const resolvedPath = useResolvedPath(to)
    const isActive = useMatch({ path: resolvedPath.pathname, end: true })

    return (
        <li className={isActive ? "active" : ""}>
            <Link to={to} {...props}>
            {children}
            </Link>
        </li>
    )
}