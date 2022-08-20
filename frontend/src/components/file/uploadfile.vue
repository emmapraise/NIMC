<template>
	<div>
		<div class="form-group">
			<!-- <b-button class="btn-sm" @click.prevent="previewFiles">
					Upload image
				</b-button> -->
			<input
				id="files"
				ref="button"
				type="file"
				hidden
				accept="image/x-png,image/gif,image/jpeg"
				name="myimage"
				@change="previewFiles"
			/>
		</div>
		<div style="width: 300px">
			<!-- <b-img
				id="myimage"
				v-bind="mainProps"
				rounded="circle"
				fluid-grow
				height="100px"
				alt="Fluid image"
				src="https://wtwp.com/wp-content/uploads/2015/06/placeholder-image-300x225.png"
				@click.prevent="previewFiles"
			/> -->
			<b-avatar
				src="https://wtwp.com/wp-content/uploads/2015/06/placeholder-image-300x225.png"
				size="7rem"
				id="myimage"
				button
				class=""
				@click.prevent="previewFiles"
			></b-avatar>
		</div>
	</div>
</template>
<script>
export default {
	name: 'UploadFile',
	props: ['file'],
	data() {
		return {
			data: {},
			mainProps: {
				blank: true,
				blankColor: '#777',
				width: 75,
				height: 100,
				class: 'm1',
			},
		};
	},
	mounted() {
		this.displayImage(this.file);
	},
	methods: {
		previewFiles(event) {
			document.getElementById('files').click();
			// this.file = event.target.files[0];
			// console.log(this.file);
			this.displayImage(event.target.files[0]);
		},
		displayImage(file) {
			if (typeof file === 'string') {
				console.log(document.getElementById('myimage').innerHTML);
				return (document.getElementById('myimage').src = file);
			}

			const reader = new FileReader();
			reader.onload = (e) => {
				document.getElementById('myimage').src = e.target.result;
			};

			reader.readAsDataURL(file);
			return;
		},
	},
};
</script>
