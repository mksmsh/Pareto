const mpSelect = document.querySelector('#id_mp');
const mdSelect = document.querySelector('#id_md');
const ttSelect = document.querySelector('#id_tt');
const mdChoices = JSON.parse('{{ md_choices_json | safe }}');
const ttChoices = JSON.parse('{{ tt_choices_json | safe }}');

mpSelect.addEventListener('change', () => {
    const selectedMpId = mpSelect.value;
    const filteredMdChoices = mdChoices.filter(choice => choice.mp_id.toString() === selectedMpId);
    const filteredTtChoices = ttChoices.filter(choice => choice.mp_id.toString() === selectedMpId);

    mdSelect.innerHTML = '<option value="">---------</option>';
    ttSelect.innerHTML = '<option value="">---------</option>';

    filteredMdChoices.forEach(choice => {
        const option = document.createElement('option');
        option.value = choice.id;
        option.textContent = choice.name;
        mdSelect.appendChild(option);
    });

    filteredTtChoices.forEach(choice => {
        const option = document.createElement('option');
        option.value = choice.id;
        option.textContent = choice.name;
        ttSelect.appendChild(option);
    });
});
