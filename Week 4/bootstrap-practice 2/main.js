function addTweets() {
    const parent = document.getElementById("tweets");
    for (i = 0; i !== 100; i++) {
        parent.innerHTML += `<div class="row border-bottom p-2">
        <div class="col-lg-1 col-3 p-0">
            <img
                src="https://pbs.twimg.com/profile_images/1407429076885794817/_CSWrfq-_400x400.jpg"
                style="
                                        height: 3rem;
                                        width: 3rem;
                                        background-color: white;
                                        border-radius: 50%;
                                    "
            ></img>
        </div>
        <div class="col-lg-11 col-9">
            <div class="row">
                <div
                    class="col-auto p-0"
                    style="
                                            margin-right: 4px;
                                            font-weight: bold;
                                        "
                >
                    Chayse Stiver
                </div>
                <div class="col-auto p-0" style="color: gray">
                    @ChayseStiver
                </div>
            </div>
            <div class="row">
                This is a test tweet: Lorem ipsum dolor sit amet
                consectetur, adipisicing elit. Qui quia neque magni quae
                voluptatem sequi porro voluptas nobis facilis culpa sit,
                ipsum ipsa vel alias modi exercitationem saepe ipsam omnis.
            </div>
            <div class="row"></div>
        </div>
    </div>
    `;
    }
}

addTweets();
