<template>
	<div>
		<b-row v-for="(item, index) in certificate" :key="index" class="my-2">
			<b-col sm="3">
				<label :for="item.label">{{ item.name }}</label></b-col
			>
			<b-col sm="9">
				<div v-if="item.type === 'select'">
					<b-form-select
						:id="item.label"
						v-model="item.value"
						required
						:options="item.options"
					></b-form-select>
				</div>
				<div v-else-if="item.type === 'file'">
					<b-form-file
						v-model="item.value"
						:state="Boolean(item.value)"
						placeholder="Choose a file or drop it here..."
						drop-placeholder="Drop file here..."
					></b-form-file>
				</div>
				<div v-else>
					<b-form-input
						:id="item.label"
						:type="item.type"
						required
					></b-form-input></div></b-col
		></b-row>
		<div class="float-right mt-2">
			<b-button variant="success">Submit</b-button>
		</div>
	</div>
</template>
<script>
export default {
	namee: 'CertificateDocument',
	data() {
		return {
			certificate: [
				{
					name: 'Upload Certificate',
					label: 'upload_cert',
					type: 'file',
					value: null,
				},
				{
					name: 'Upload Transcript',
					label: 'upload_transcript',
					type: 'file',
					value: null,
				},
			],
		};
	},
};
</script>
