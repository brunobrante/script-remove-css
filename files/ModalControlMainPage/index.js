import React from 'react';
import styles from './ModalControlMainPage.module.css'

export default function ModalControlMainPage() {
	return (
		<>
			<div className={styles.modal_control_menu}>
				<div className={styles.modal_content_header}>
					<i className="icon_close_thinner"></i>
					<h1><i className="icon_barcode"></i> Controle | Menu</h1>
					<h2>Aqui é o local onde você pode <b>ADICIONAR</b> regiões.</h2>
				</div>
				<div className={`${styles.modal_content_body} scroll`}>
					<div className={styles.message}></div>
					<form action="">
						<div className={styles.content_product}>
							<div className={styles.photo_product}><img src="" alt="" /></div>
							<div className={styles.content_product_info}>
								<div className={styles.modal_item}>
									<h2>Código de barras: </h2>
									<p name="barcode"></p>
								</div>
								<div className={styles.modal_item}>
									<h2>Nome:</h2>
									<p name="name"></p>
								</div>
								<div className={styles.modal_item}>
									<h2>Tipo:</h2>
									<p name="type"></p>
								</div>
								<div className={styles.modal_item}>
									<h2>Preço:</h2>
									<p name="price"></p>
								</div>
								<div className={styles.modal_item}>
									<h2>Oferta:</h2>
									<p name="offer"></p>
								</div>
							</div>
						</div>
						<div>
							<p className={styles.content_text}>
								Essa oferta já está programada para finalizar no dia <b name="date_limit"></b>, caso queira editar será
								cobrado apenas os dias adicionais.
							</p>
							<p className={styles.content_text} data-tickets="">Você tem <b>200</b>disponível na sua conta.</p>
						</div>
						<div className={styles.modal_row_item}>
							<div className={styles.modal_item}>
								<h2>Selecione o tempo:</h2>
								<select name="date_type" >
									<option value="1day">1 dia</option>
									<option value="1week">1 semana</option>
									<option value="1month">1 mês</option>
									<option value="date">Selecionar o tempo</option>
								</select>
							</div>
							<div className={styles.modal_item}>
								<h2>Data:</h2>
								<input type="text" className={styles.mask_date} name="date_limit" min="" />
							</div>
						</div>
						<div className={styles.tickets_balance}>
							<h2>Essa oferta te custará:</h2>
							<p name="ticket_cost">1 ticket</p>
						</div>
						<div className={styles.tickets_balance}>
							<h2>Seu saldo futuro:</h2>
							<p name="ticket_future"></p>
						</div>
						<p className={styles.content_text}>Essa oferta sairá do topo do menu no dia <b
							name="date_future"></b></p>
						<div className={styles.content_button}>
							<button className={`${styles.button_pattern} gradient`} type="submit">Adicionar</button>
							<button className={`${styles.button_pattern} red`} type="button">Desabilitar</button>
							<button className={`${styles.button_pattern} gradient`} type="submit">Editar</button>
						</div>
					</form>
				</div>
			</div>
		</>
	);
}