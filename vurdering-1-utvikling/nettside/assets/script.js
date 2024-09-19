let footer = document.getElementById("footer");
if (footer) {
    let tilbakeElement = document.createElement("div");
    tilbakeElement.classList.add("til-toppen-knapp");
    tilbakeElement.textContent = "Til toppen";
    tilbakeElement.onclick = () => {
        window.scrollTo({ top: 0 });
    };
    footer.appendChild(tilbakeElement);
}
