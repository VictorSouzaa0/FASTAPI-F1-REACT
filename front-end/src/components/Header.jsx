import React from 'react'
import styles from '../modules/Header.module.css'
import logo from "../assets/F1-Logo.png"


export default function Header() {

  return (
    <div class={styles.header}>
        <img src={logo} alt="" />
        <a href="/">
            <button>Teams</button>
        </a>
        <a href="/drivers/">
            <button>Drivers</button>
        </a>
    </div>
  )
}
