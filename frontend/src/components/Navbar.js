import React, { useState } from "react";
import { AiOutlineBars, AiFillGithub } from "react-icons/ai";


const Navbar = () => {

    const [toggleDropdown, setToggleDropdown] = useState(false);

    function handleMenuClick() {
        setToggleDropdown(prevDropdownState => !prevDropdownState)
    }


    return (
        <nav className="navbar">
            <AiOutlineBars size="35px" onClick={() => handleMenuClick()} style={{ cursor: 'pointer' }} className="navbar-menu"/>  
            <h1 className="navbar-title">FixIt</h1>
            <a href="https://github.com/NickStrauch13/IDS706-Individual-Project-4"><AiFillGithub size="35px" className="navbar-github"/></a>
            
        </nav>
    )
}

export default Navbar