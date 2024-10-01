document.addEventListener('DOMContentLoaded', () => {
            const filterInput = document.getElementById('filter');
            const sortSelect = document.getElementById('sort');
            const staffContainer = document.getElementById('staff-container');

            function updateCards() {
                const filterText = filterInput.value.toLowerCase();
                const sortOrder = sortSelect.value;
                const cards = Array.from(staffContainer.getElementsByClassName('card'));

                // Filter
                cards.forEach(card => {
                    const name = card.getAttribute('data-name').toLowerCase();
                    card.style.display = name.includes(filterText) ? 'inline-block' : 'none';
                });

                // Sort
                const sortedCards = cards.sort((a, b) => {
                    const nameA = a.getAttribute('data-name').toLowerCase();
                    const nameB = b.getAttribute('data-name').toLowerCase();
                    if (sortOrder === 'asc') {
                        return nameA.localeCompare(nameB);
                    } else {
                        return nameB.localeCompare(nameA);
                    }
                });

                // Re-append sorted cards to container
                sortedCards.forEach(card => staffContainer.appendChild(card));
            }

            filterInput.addEventListener('input', updateCards);
            sortSelect.addEventListener('change', updateCards);
        });

function changeTheme(theme) {
                document.body.className = theme;
            }