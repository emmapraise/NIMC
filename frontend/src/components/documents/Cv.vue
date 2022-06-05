<template>
	<div>
		<b-row v-for="(item, index) in cv_tab" :key="index">
			<b-col sm="3">
				<label :for="item.label">{{ item.name }}</label>
			</b-col>
			<b-col sm="9">
				<b-form-file
					v-model="item.value"
					:state="Boolean(item.value)"
					placeholder="Choose a file or drop it here..."
					drop-placeholder="Drop file here..."
				></b-form-file>
			</b-col>
		</b-row>
		<div class="float-right mt-3">
			<b-button variant="success">Submit</b-button>
		</div>
	</div>
</template>
<script>
export default {
	name: 'CVComponent',
	data() {
		return {
			cv_tab: [
				{
					name: 'Upload CV',
					label: 'upload_cv',
					type: 'file',
					value: '',
				},
			],
		};
	},
};
</script>
