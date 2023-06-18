function push(id) {
	alert(id);
}

const url = "https://script.google.com/macros/s/AKfycbwnzaNnVT1wYH7StAFkqWehJCPceK6DLbOaB9YrvCPWkq7yDwRIv803Fub8ijGeiKAniQ/exec";

async function getdata() {
	const response = await fetch(url);
	const result = await response.json();
	console.log(result);
	result.forEach(dic => {
		id = dic["id"];
		stat = dic["status"];
		$("#"+id).addClass(stat);

		// 部屋の状態が変わったらアイコンの表示非表示も変更する
		const cnt = id.split("_").length	// _で区切られた要素の数
		if (cnt==3) {
			$("#"+id+"_cleaning").addClass("hide");
			$("#"+id+"_caution").addClass("hide");
			if (stat != "available") {
				$("#"+id+"_"+stat).removeClass("hide");
			}
		}
	});
}

getdata();


// class=man（人のマーク）をクリックしたときの関数
$(".man").on("click", function() {
    let room_id = "#" + $(this).attr('id');
	let area_id = room_id.slice(0, room_id.length-2);
	let is_area_available;
    console.log(area_id);
	if ($(area_id).hasClass("cleaning")==false && $(area_id).hasClass("caution")==false) {
		is_area_available = true;
	} else {
		is_area_available = false
	}
	let is_busy = $(room_id).hasClass("busy");
	if (is_area_available == true) {
		if (is_busy == true) {
			$(room_id).removeClass("busy");
			$(room_id).addClass("empty");
		} else {
			$(room_id).removeClass("empty");
			$(room_id).addClass("busy");
		}
	}
});


// class=btn（ボタン）をクリックしたときの関数
$(".btn").on("click", function() {
    let myclass = $(this).attr('id');
	let area_id = "#3階_南東_男";
	$(area_id).removeClass("available");
	$(area_id).removeClass("cleaning");
	$(area_id).removeClass("caution");
	$(area_id).addClass(myclass);

	$(area_id+"_cleaning").addClass("hide");
	$(area_id+"_caution").addClass("hide");
	$(area_id+"_"+myclass).removeClass("hide");
});
