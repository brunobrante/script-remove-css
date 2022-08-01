import React from 'react';
import styles from './ModalCreditCard.module.css'

export default function ModalCreditCard() {
	return (
		<>
			<div className={styles.modal_credit_card}>
				<div className={styles.modal_content_header}>
					<i className="icon_close_thinner"></i>
					<h1><i className="icon_credit_cards"></i>Forma de pagamento</h1>
					<h2>Aqui é o local onde você pode <b>ADICIONAR</b> um pagamento.</h2>
				</div>
				<div className={`${styles.modal_content_body} scroll`}>
					<div className={styles.message}></div>
					<form action="">
						<div className={styles.credit_card}>
							<div className={styles.front_credit_card}>
								<div className="icon_chip"></div>
								<h1 className={styles.card_number} id="number">5348 0637 4265 2223</h1>
								<div className={styles.content_validate}>
									<span className={styles.text_validate}>Válido
										até</span>
									<h2 className={styles.date_validate} id="expDate">05/21</h2>
								</div>
								<h2 className={styles.card_name} id="name">Bruno V B Goncalves</h2>
								<div className="icon_operator"></div>
							</div>
							<div className={styles.back_credit_card}>
								<div className={styles.style_magnet}></div>
								<div className={styles.content_cvv}>
									<div className={styles.style_cvv}></div>
									<h2 className={styles.number_cvv} id="cvv">862</h2>
								</div>
								<div className="icon_operator"></div>
							</div>
						</div>
						<div className={styles.modal_item}>
							<h2>Número:</h2>
							<input type="text" name="number" className={styles.mask_card} />
						</div>
						<div className={styles.modal_item}>
							<h2>Nome no cartão:</h2>
							<input type="text" name="name" />
						</div>
						<div className={styles.modal_row_item}>
							<div className={styles.modal_item}>
								<h2>Validade:</h2>
								<input type="text" name="expDate" className={styles.mask_card_date} />
							</div>
							<div className={styles.modal_item}>
								<h2>CVV:</h2>
								<input type="text" name="cvv" className={styles.mask_card_cvv} />
							</div>
						</div>
						<button className={`${styles.button_pattern} gradient`} type="submit">Adicionar</button>
					</form>
				</div >
			</div >
		</>
	);
}