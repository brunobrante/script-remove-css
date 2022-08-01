import React from 'react';
import styles from './Footer.module.css'

export default function Footer() {
	return (
		<>
			<footer className={styles.main_footer}>
				<div className={styles.footer_content_name}>
					<i className={styles.icon_company}></i>
					<h1>Vai <b>Comprar ?</b></h1>
				</div>
				<p>Copyright &copy {(new Date()).getFullYear()} - Hipótese - Todos os direitos reservados</p>
			</footer>
		</>
	);
}