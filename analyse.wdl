workflow myWorkflow {
    call analyseVcf
}

task analyseVcf {
    File inputFile
    File outputFile
    
    runtime {
        docker: "muzic194/vcf-analyse"
    }
    command {
        python3 /script/analyse.py ${inputFile} ${outputFile}
    }
    output {
        String out = "${outputFile}"
    }
}
