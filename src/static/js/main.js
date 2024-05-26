import { postData } from './api.js';

// VARIABLES

const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const optionsButton = document.getElementById('optionsButton');
const optionsWindows = document.getElementById('optionsWindow');

const searchDepth = document.getElementById('searchDepth');
const searchDepthValue = document.getElementById('searchDepthValue');
const phrasesNumber = document.getElementById('phrasesNumber');
const phrasesNumberValue = document.getElementById('phrasesNumberValue');
const multipleSearchingCheckbox = document.getElementById('multipleSearchingCheckbox');

const playlistTable = document.getElementById('playlistTable');

// FUNCTIONS

function updateValues() {
    searchDepthValue.textContent = searchDepth.value;
    phrasesNumberValue.textContent = phrasesNumber.value;
}

function collapseSearchOptions() {
    new bootstrap.Collapse(searchInput).hide();
    new bootstrap.Collapse(optionsButton).hide();
    new bootstrap.Collapse(optionsWindows, {
        toggle: false
    }).hide();
}

async function handleCreatePlaylist(tracksList) {
    try {
        const playlistName = document.getElementById('playlistName');
        const formData = {
            playlistName: playlistName.value,
            'tracks': tracksList
        }

        const link = await postData('/create_playlist', formData);

        new bootstrap.Collapse(document.getElementById('playlistName')).hide();
        window.open(link, '_blank')

        const createPlaylistButton = document.getElementById('createPlaylistButton');
        createPlaylistButton.textContent = 'Open Playlist';
        createPlaylistButton.className = 'btn btn-primary px-2 gap-3';
        createPlaylistButton.onclick = () => window.open(link, '_blank');
    } catch (error) {
        console.error('Failed to search tracks:', error);
        searchButton.innerHTML = `Failed to search, try again`;
        searchButton.disabled = false;
    } finally {
        searchButton.innerHTML = 'Search for tracks ♪';
        searchButton.disabled = false;
    }
}

async function handleSearch() {
    collapseSearchOptions();

    searchButton.innerHTML =
        `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Finding tracks...`;
    searchButton.disabled = true;

    try {
        const formData = {
            searchQuery: searchInput.value,
            multipleSearching: multipleSearchingCheckbox.checked,
            searchDepth: searchDepth.value,
            phrasesNumber: phrasesNumber.value
        };

        const data = await postData('/searching_tracks', formData);
        const tracksList = data.tracks;

        renderPlaylistTable(tracksList);
        collapseSearchOptions();

        const createPlaylistButton = document.getElementById('createPlaylistButton');
        createPlaylistButton.addEventListener('click', () => {
            handleCreatePlaylist(tracksList)
        });

    } catch (error) {
        console.error('Failed to search tracks:', error);
        searchButton.innerHTML = `Failed to search, try again`;
        searchButton.disabled = false;
    } finally {
        searchButton.innerHTML = 'Search for tracks ♪';
        searchButton.disabled = false;
    }
}

function renderPlaylistTable(tracksList) {
    let buttonsHTML = `
        <div class="d-flex justify-content-end mb-3">
            <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
                <input type="search" class="form-control collapse collapse-horizontal show" placeholder="Playlist name..." aria-label="Search" id="playlistName">
            </form>
            <button class="btn btn-success px-2 gap-3" id="createPlaylistButton">Create playlist</button>
        </div>`;

    let tableHTML = `
        <ul class="list-group">
            <li class="list-group-item">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Track Name</th>
                            <th scope="col">Artist</th>
                            <th scope="col">Link</th>
                        </tr>
                    </thead>
                    <tbody class="table-group-divider">`;

    Object.entries(tracksList).forEach(([track, details]) => {
        tableHTML += `
            <tr>
                <td>${track++}</td>
                <td>${details.title}</td>
                <td>${details.artist}</td>
                <td><a href="${details.uri}" target="_blank" class="link-no-underline">🔗</a></td>
            </tr>`;
    });

    tableHTML += '</tbody></table></li></ul>';

    playlistTable.innerHTML = buttonsHTML + tableHTML;
}

// EVENT LISTENERS

updateValues();

searchDepth.addEventListener('input', updateValues);
phrasesNumber.addEventListener('input', updateValues);
searchButton.addEventListener('click', handleSearch);