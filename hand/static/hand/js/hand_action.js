
const pre_btn = document.getElementById('go-to-pre')
pre_btn.addEventListener('click', e => {
   e.preventDefault();
   // Form update
   let hand_info = document.querySelectorAll('.hand-info');
   hand_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.remove('d-none');
   });

   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.add('d-none');
   });

   let turn = document.querySelectorAll('.turn-info');
   turn.forEach(upd => {
      upd.classList.add('d-none')
   });

   let river = document.querySelectorAll('.river-info');
   river.forEach(upd => {
      upd.classList.add('d-none')
   });

   //Navbar update
   let inf_btn = document.getElementById('go-to-info-li');
   inf_btn.classList.remove('active');

   let pre_btn = document.getElementById('go-to-pre-li');
   pre_btn.classList.add('active');

   let flop_btn = document.getElementById('go-to-flop-li');
   flop_btn.classList.remove('active');

   let turn_btn = document.getElementById('go-to-turn-li')
   turn_btn.classList.remove('active');

   let river_btn = document.getElementById('go-to-river-li');
   river_btn.classList.remove('active');

   //h5 update
   let h5_info = document.getElementById('h5-info');
   h5_info.classList.add('d-none')

   let h5_pre = document.getElementById('h5-pre');
   h5_pre.classList.remove('d-none')

   let h5_flop = document.getElementById('h5-flop');
   h5_flop.classList.add('d-none')

   let h5_turn = document.getElementById('h5-turn');
   h5_turn.classList.add('d-none')

   let h5_river = document.getElementById('h5-river');
   h5_river.classList.add('d-none')

})


const flop_btn = document.getElementById('go-to-flop')
flop_btn.addEventListener('click', e => {
   e.preventDefault();
   //Flop show
   let flop_cards = document.getElementById('flop-cards')
   flop_cards.classList.remove('d-none')
   //Turn hide
   let turn_card = document.getElementById('turn-card')
   turn_card.classList.add('d-none')
   //River hide
   let river_card = document.getElementById('river-card')
   river_card.classList.add('d-none')
   // Form update
   let hand_info = document.querySelectorAll('.hand-info');
   hand_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.remove('d-none');
   });

   let turn = document.querySelectorAll('.turn-info');
   turn.forEach(upd => {
      upd.classList.add('d-none')
   });

   //Navbar update
   let river = document.querySelectorAll('.river-info');
   river.forEach(upd => {
      upd.classList.add('d-none')
   });
   let inf_btn = document.getElementById('go-to-info-li');
   inf_btn.classList.remove('active');

   let pre_btn = document.getElementById('go-to-pre-li');
   pre_btn.classList.remove('active');

   let flop_btn = document.getElementById('go-to-flop-li');
   flop_btn.classList.add('active');

   let turn_btn = document.getElementById('go-to-turn-li')
   turn_btn.classList.remove('active');

   let river_btn = document.getElementById('go-to-river-li');
   river_btn.classList.remove('active');

})

const turn_btn = document.getElementById('go-to-turn')
turn_btn.addEventListener('click', e => {
   e.preventDefault()
   //Flop hide
   let flop_cards = document.getElementById('flop-cards')
   flop_cards.classList.add('d-none')
   //Turn show
   let turn_card = document.getElementById('turn-card')
   turn_card.classList.remove('d-none')
   //River hide
   let river_card = document.getElementById('river-card')
   river_card.classList.add('d-none')
   // Form update
   let hand_info = document.querySelectorAll('.hand-info');
   hand_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.add('d-none');
   });

   let turn = document.querySelectorAll('.turn-info');
   turn.forEach(upd => {
      upd.classList.remove('d-none')
   });

   let river = document.querySelectorAll('.river-info');
   river.forEach(upd => {
      upd.classList.add('d-none')
   });

   //Navbar update
   let inf_btn = document.getElementById('go-to-info-li');
   inf_btn.classList.remove('active');

   let pre_btn = document.getElementById('go-to-pre-li');
   pre_btn.classList.remove('active');

   let flop_btn = document.getElementById('go-to-flop-li');
   flop_btn.classList.remove('active');

   let turn_btn = document.getElementById('go-to-turn-li')
   turn_btn.classList.add('active');

   let river_btn = document.getElementById('go-to-river-li');
   river_btn.classList.remove('active');
})

const river_btn = document.getElementById('go-to-river');
river_btn.addEventListener('click', e => {
   e.preventDefault()
   //Flop hide
   let flop_cards = document.getElementById('flop-cards')
   flop_cards.classList.add('d-none')
   //Turn hide
   let turn_card = document.getElementById('turn-card')
   turn_card.classList.add('d-none')
   //River show
   let river_card = document.getElementById('river-card')
   river_card.classList.remove('d-none')
   // Form update
   let hand_info = document.querySelectorAll('.hand-info');
   hand_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.add('d-none');
   });

   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.add('d-none');
   });

   let turn = document.querySelectorAll('.turn-info')
   turn.forEach(upd => {
      upd.classList.add('d-none')
   });

   let river = document.querySelectorAll('.river-info');
   river.forEach(upd => {
      upd.classList.remove('d-none')
   });

   //Navbar update

   let inf_btn = document.getElementById('go-to-info-li');
   inf_btn.classList.remove('active');

   let pre_btn = document.getElementById('go-to-pre-li');
   pre_btn.classList.remove('active');
   
   let flop_btn = document.getElementById('go-to-flop-li');
   flop_btn.classList.remove('active');

   let turn_btn = document.getElementById('go-to-turn-li')
   turn_btn.classList.remove('active');

   let river_btn = document.getElementById('go-to-river-li');
   river_btn.classList.add('active');

})

// Hand display update

const flop_act = document.querySelectorAll('#flop-action')
flop_act.forEach(act => {
   if (act.textContent == "None:") {
      let flop_disp = document.getElementById('flop-display');
      flop_disp.classList.add('d-none');
      
      let turn_disp = document.getElementById('turn-display');
      turn_disp.classList.add('d-none');

      let river_disp = document.getElementById('river-display');
      river_disp.classList.add('d-none')
   }
})

const turn_act = document.querySelectorAll('#turn-action')
turn_act.forEach(act => {
   if (act.textContent == "None:") {
      let turn_disp = document.getElementById('turn-display');
      turn_disp.classList.add('d-none');

      let river_disp = document.getElementById('river-display');
      river_disp.classList.add('d-none')
   }
})

const river_act = document.querySelectorAll('#river-action')
river_act.forEach(act => {
   if (act.textContent == "None:") {

      let river_disp = document.getElementById('river-display');
      river_disp.classList.add('d-none')
   }
})

