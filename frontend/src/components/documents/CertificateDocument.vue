<template>
	<div>
		<b-row v-for="(item, index) in certificate" :key="index" class="my-2">
			<b-col sm="3">
				<label :for="item.label">{{ item.name }}</label></b-col
			>
			<b-col sm="9">
				<div v-if="item.type === 'file'">
					<b-form-file
						v-model="item.value"
						:state="Boolean(item.value)"
						placeholder="Choose a file or drop it here..."
						drop-placeholder="Drop file here..."
					></b-form-file>
				</div>
				<div v-else-if="item.type === 'combobox'">
					<user-combobox-vue :citizens="citizens" />
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
import UserComboboxVue from '../combobox/UserCombobox.vue';
export default {
	namee: 'CertificateDocument',
	props: ['citizens'],
	components: { UserComboboxVue },
	data() {
		return {
			certificate: [
				{
					name: 'User',
					label: 'citizen',
					type: 'combobox',
					value: '',
				},
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
