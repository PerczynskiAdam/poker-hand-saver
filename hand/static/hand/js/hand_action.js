const pre_btn = document.getElementById('go-to-pre')
pre_btn.addEventListener('click', e => {
   e.preventDefault();
   const hand_info = document.querySelectorAll('.hand-info');
   hand_info.forEach(upd => {
      upd.classList.add('d-none');
   });
   let pre_btn = document.getElementById('go-to-pre');
   pre_btn.classList.add('d-none');

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.remove('d-none');
   });

   let flop_btn = document.getElementById('go-to-flop');
   flop_btn.classList.remove('d-none');

   // let hand_info_btn_up = document.getElementById('hand-info-btn');
   // hand_info_btn_up.classList.remove('d-none');


})


const flop_btn = document.getElementById('go-to-flop')
flop_btn.addEventListener('click', e => {
   e.preventDefault();
   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.remove('d-none');
   });
   // let hand_info_btn_up = document.getElementById('hand-info-btn');
   // hand_info_btn_up.classList.add('d-none');

   let pre_info = document.querySelectorAll('.pre-info');
   pre_info.forEach(upd => {
      upd.classList.add('d-none');
   });
   // let pre_btn = document.getElementById('go-to-pre');
   // pre_btn.classList.remove('d-none');
   let turn_btn = document.getElementById('go-to-turn')
   turn_btn.classList.remove('d-none')

   let flop_btn = document.getElementById('go-to-flop');
   flop_btn.classList.add('d-none');
})

const turn_btn = document.getElementById('go-to-turn')
turn_btn.addEventListener('click', e => {
   e.preventDefault()
   let turn = document.querySelectorAll('.turn-info');
   turn.forEach(upd => {
      upd.classList.remove('d-none')
   });
   let flop = document.querySelectorAll('.flop-info');
   flop.forEach(upd => {
      upd.classList.add('d-none');
   });
   let river_btn = document.getElementById('go-to-river')
   river_btn.classList.remove('d-none');
   let turn_btn = document.getElementById('go-to-turn')
   turn_btn.classList.add('d-none');
})

const river_btn = document.getElementById('go-to-river');
river_btn.addEventListener('click', e => {
   e.preventDefault()
   let river = document.querySelectorAll('.river-info');
   river.forEach(upd => {
      upd.classList.remove('d-none')
   });
   let turn = document.querySelectorAll('.turn-info')
   turn.forEach(upd => {
      upd.classList.add('d-none')
   });

   let river_btn = document.getElementById('go-to-river');
   river_btn.classList.add('d-none');


})

